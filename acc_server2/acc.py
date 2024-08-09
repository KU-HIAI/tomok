# python
from typing import Dict, List
from dataclasses import asdict
from contextvars import ContextVar
import logging
from copy import deepcopy
import os
import json
import random

# 3rd-party
import numpy as np
from hydra.utils import to_absolute_path, instantiate
from utils_crypt import Crypt

# framework
from tomok import IFCReader, RuleIFCController, RuleUnitController, ACCController


logger = logging.getLogger(__name__)
ifc_path = "uploads/"
temp_files = "./temp_files"
os.makedirs(ifc_path, exist_ok=True)
CRYPT = ContextVar("crypt", default=None)
RIC = ContextVar("RuleIFCController", default=None)
AC = ContextVar("ACCController", default=None)


def acc_init(app):
    config = app["config"]
    crypt = Crypt(config.server.api_secret)
    CRYPT.set(crypt)
    acc_relpath = os.path.relpath(to_absolute_path(temp_files), os.getcwd())
    ac = ACCController(
        resource_path=temp_files,
        rule_file="tree_temp2.csv",
        module_file="module_temp.csv",
    )
    AC.set(ac)


def upload(user, *args, **kwargs) -> Dict:
    crypt = CRYPT.get()
    # get token and expired date
    token_dict = crypt.file_to_token(kwargs["ifcfile"].filename, expired_days=1.0)
    token = token_dict["token"]
    expired_datetime = token_dict["expired_datetime"]
    filepath = to_absolute_path(ifc_path + token)
    # write ifc file
    with open(filepath, "wb") as fp:
        fp.write(kwargs["ifcfile"].file.read())
    try:
        # file read test
        reader = IFCReader(filepath)
        reader.get_products()
    except:
        # if not readable
        os.remove(filepath)
        return {
            "status": 400,
            "detail": "uploaded IFC file is not readable. please check IFC file or contact developer.",
        }
    # return info
    return {
        "token": token,
        "expired_datetime": expired_datetime,
        "status": 200,
        "detail": "ok",
    }


def get_modules(user) -> Dict:
    ac = AC.get()
    orders = ac.get_execution_orders()
    temp = {}
    temp["0"] = orders
    return {
        "modules": temp,
        "status": 200,
        "detail": "ok",
    }


def verify(user, *args, **kwargs) -> Dict:
    crypt = CRYPT.get()
    ric = RIC.get()

    token = kwargs["body"]["ifctoken"]
    rule_index = kwargs["body"]["ruleid"]
    guid = kwargs["body"]["guid"]

    filepath = to_absolute_path(ifc_path + token)
    reader = IFCReader(filepath)

    results, results_str = ric.verify(reader, rule_index, guid, return_results=True)

    return {
        "results": [result.to_json() for result in results],
        "detail": "ok",
        "status": 200,
    }


def verify_module(user, *args, **kwargs) -> Dict:
    crypt = CRYPT.get()
    # ac = AC.get()
    ac = ACCController(
        resource_path=temp_files,
        rule_file="tree_temp2.csv",
        module_file="module_temp.csv",
    )

    token = kwargs["body"]["ifctoken"]
    module_index = kwargs["body"]["module_index"]
    subtype = kwargs["body"]["subtype"]

    filepath = to_absolute_path(ifc_path + token)

    # ACC
    ac.load_ifc_file(filepath)
    ac.set_subtype(subtype)
    entities = ac.search_entities()
    print(len(entities))

    results = ac.run_verification()

    return {
        "results": results,
        "detail": "ok",
        "status": 200,
    }
