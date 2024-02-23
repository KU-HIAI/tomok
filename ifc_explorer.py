import base64
import streamlit as st
from tomok import IFCReader
from tomok import RuleUnitController

def dict_generator(indict, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                for d in dict_generator(value, pre + [key]):
                    yield d
            elif isinstance(value, list) or isinstance(value, tuple):
                for v in value:
                    for d in dict_generator(v, pre + [key]):
                        yield d
            else:
                yield pre + [key, value]
    else:
        yield pre + [indict]

def get_subtypes(reader):
    keys = list(reader.subtype_product_cache.keys())
    if None in keys:
        keys.remove(None)
    if '레벨:8MM 헤드' in keys:
        keys.remove('레벨:8MM 헤드')
    return keys

def get_entities(reader, subtype, rulecodes):
    entities = []
    ruleunits = {}
    for entity in reader.subtype_product_cache[subtype]:
        for pset_name in entity.property_set_names:
            properties = entity[pset_name].get_properties()
            if('Ruleset code' in properties.keys()):
                ruleset_code = properties['Ruleset code']['value']
                # print(ruleset_code)
                # print(ruleset_code in rulecodes)
                if ruleset_code in rulecodes:
                    # print(rulecodes[ruleset_code].filepath)
                    with open(rulecodes[ruleset_code].filepath) as f:
                        b64_text = base64.b64encode(f.read().encode()).decode()
                        href = f'<a href="data:file/txt;base64,{b64_text}" download="{rulecodes[ruleset_code].filename}">룰 유닛 파일 다운로드</a>'
                        # ruleunits.append({'ruleset': ruleset_code, 'file': href})
                        if ruleset_code not in ruleunits:
                            ruleunits[ruleset_code] = href
        processed_entity = {
            'entity': str(entity),
            'entity_instances': str(entity.tree['entity_instances']),
        }
        entities.append(processed_entity)
    ruleunit_list = [{'ruleunit':k, 'file':v} for k, v in ruleunits.items()]
    return entities, ruleunit_list

def main():
    st.markdown("""# 확장 IFC 룰 유닛 다운로더 🪡
                
- 본 프로그램은 확장 IFC(Extended Industry Foundation Classes)을 읽고, 확장 IFC 파일의 subtype 별로 가지고 있는 entity와 해당 entity를 검증할 때 사용하는 룰 유닛을 쉽게 다운받을 수 있는 도구 입니다.
""")

    uploaded_file = st.file_uploader("확장 IFC 파일 업로드", type='ifc')
    st.markdown("예시 파일 [다운로드](https://drive.google.com/file/d/1WBy_qUhjumZCoHjpGsJRdQyayZ2UGq5v/view?usp=sharing)")
    
    if uploaded_file:
        with st.spinner('IFC 파일 분석중 입니다...'):
            ruc = RuleUnitController('./api_server/ruleunits')
            rulecodes = {ru[3]:ru[4] for ru in dict_generator(ruc.ruleunits_dict)}

            with open('temp.ifc', 'wb') as f:
                f.write(uploaded_file.getbuffer())

            reader = IFCReader('temp.ifc')

        subtypes = get_subtypes(reader)

        for subtype in subtypes:
            entities, ruleunit_list = get_entities(reader, subtype, rulecodes)

            st.markdown('---')
            st.markdown(f'## 서브타입: {subtype}')
            st.markdown('### entity 리스트')
            st.dataframe(entities)
            st.markdown('### 룰 유닛 다운로드 리스트')
            for ruleunit in ruleunit_list:
                name = ruleunit['ruleunit']
                link = ruleunit['file']
                st.markdown(f'- {name} {link}', unsafe_allow_html=True)
            # st.dataframe(ruleunit_list)

if __name__ == '__main__':
    main()