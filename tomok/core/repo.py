import os
import shutil
import subprocess


TF_REPO_ID = "tomok_table_functions"

def prepare_tf_repo(overwrite, TF_REPO_TOKEN):
    if overwrite and os.path.exists(TF_REPO_ID):
        shutil.rmtree(TF_REPO_ID)

    # Clone the repository
    url = f'https://tomoknetwork:{TF_REPO_TOKEN}@github.com/tomoknetwork/{TF_REPO_ID}'
    process = subprocess.Popen(['git', 'clone', url], stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error is not None:
        print("Error occurred while cloning the repo:", error)
    else:
        print("Repo successfully cloned.")


def tf_commit(target_class, target_path, TF_REPO_TOKEN, commit_msg=None, source_file='working.py'):
    full_path = os.path.join(TF_REPO_ID, target_path)
    os.makedirs(full_path, exist_ok=True)
    filename = f'{target_class.__class__.__name__}.py'
    if filename.lower().startswith('kds') and '_' in filename:
        filename = '_'.join(filename.split('_')[1:])
    if filename.lower().startswith('kcs') and '_' in filename:
        filename = '_'.join(filename.split('_')[1:])
    target_file_path = os.path.join(full_path, filename)
    
    shutil.copyfile(source_file, target_file_path)
    
    # git commit 및 push
    try:
        subprocess.check_call(['git', '-C', TF_REPO_ID, 'add', '.'])
        if not commit_msg:
            subprocess.check_call(['git', '-C', TF_REPO_ID, 'commit', '-m', f'Add {target_file_path} file'])
        else:
            subprocess.check_call(['git', '-C', TF_REPO_ID, 'commit', '-m', commit_msg])
        subprocess.check_call(['git', '-C', TF_REPO_ID, 'push'])
    except subprocess.CalledProcessError as e:
        print(f'An error occurred: {str(e)}')