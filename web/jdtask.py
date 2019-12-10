# 京东数据获取

import logging
import json
import tglm.jd.rest

tglm.jd.setDefaultAppInfo("23735405505f55bfb73a7470f2713c67", "036cb8f415eb4485b82ad51e53cd3240")


def getcategory():
    req = tglm.jd.rest.JdUnionOpenCategoryGoodsGetRequest()
    req.parentId = 0
    req.grade = 0
    try:
        result = req.getResponse()
        #在这里处理获取到的结果
        jsonobj = json.loads(result)
    except Exception as e:
        logging.exception(e)
