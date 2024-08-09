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
from tomok import IFCReader, RuleIFCController


logger = logging.getLogger(__name__)
ifc_path = "uploads/"
os.makedirs(ifc_path, exist_ok=True)
CRYPT = ContextVar("crypt", default=None)
RIC = ContextVar("RuleIFCController", default=None)


def ifc_init(app):
    config = app["config"]
    crypt = Crypt(config.server.api_secret)
    CRYPT.set(crypt)
    rule_ifc_relpath = os.path.relpath(
        to_absolute_path(config.server.rule_ifc_dir), os.getcwd()
    )
    ric = RuleIFCController(rule_ifc_relpath, None, "local")
    RIC.set(ric)


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


def get_rules(user) -> Dict:
    ric = RIC.get()
    return {
        "rules": json.loads(
            ric.rules_df.reset_index().to_json(
                force_ascii=False, orient="records", indent=4
            )
        ),
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


def verify_all(user, *args, **kwargs) -> Dict:
    crypt = CRYPT.get()
    ric = RIC.get()

    token = kwargs["body"]["ifctoken"]
    guid = kwargs["body"]["guid"]

    filepath = to_absolute_path(ifc_path + token)
    reader = IFCReader(filepath)

    results, results_str = ric.verify_all(reader, guid, return_results=True)

    return {
        "results": [result.to_json() for result in results],
        "detail": "ok",
        "status": 200,
    }
