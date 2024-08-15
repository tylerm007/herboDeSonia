
from functools import wraps
import logging
from pathlib import Path
from flask_cors import cross_origin
import safrs
from flask import request, jsonify
from flask_jwt_extended import get_jwt, jwt_required, verify_jwt_in_request
from safrs import jsonapi_rpc
from sqlalchemy import and_, or_
from sqlalchemy.sql import text
from database import models
from api.system.custom_endpoint import CustomEndpoint, DotDict
from security.system.authorization import Security
from api.system.javascript import JavaScript
import json


app_logger = logging.getLogger(__name__)

db = safrs.DB  # valid only after is initialized, above
session = db.session

def add_service(app, api, project_dir, swagger_host: str, PORT: str, method_decorators ):
    pass


    #ResourceType: JavaScript ResourceName: JS_ExtProp isActive: True
    @app.route('/rest/default/herboDeSonia/v1/js_extprop', methods=['GET','OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def js_extprop():
        js = get_JS_ExtProp(request)
        return JavaScript(javaScript=js).execute(request)

    def get_JS_ExtProp(request):
        
        args = request.args
        argValue = args.get("filter", "1=1")
        """
        #return 'resourceName=req.urlParameters.filter+"";
        extendedProperties = listenerUtil.getExtendedPropertiesFor("v1", resourceName);
        if (extendedProperties) and extendedProperties.MyExtension):

            result = {
        # The code snippet you provided is defining a function `get_JS_ExtProp` that processes a request to
        # retrieve extended properties for a JavaScript resource. The function is extracting query
        # parameters from the request, then attempting to retrieve extended properties based on certain
        # conditions.
                isReadOnly : extendedProperties.isReadOnly,
                subLayoutClassName : extendedProperties.subLayoutClassName,
                displaySubFormClassName: extendedProperties.displaySubFormClassName,
                querySubFormClassName: extendedProperties.querySubFormClassName,
                insertNotAllow: extendedProperties.insertNotAllow,
                deleteNotAllow: extendedProperties.deleteNotAllow,
                updateNotAllow: extendedProperties.updateNotAllow,
                insertAllow: extendedProperties.insertAllow,
                deleteAllow: extendedProperties.deleteAllow,
                updateAllow: extendedProperties.updateAllow,
                multiSelect: extendedProperties.multiSelect,
                resourceName: req.urlParameters.filter,
                extraFilterToSelect:extendedProperties.extraFilterToSelect,
                tagsForVisibility:extendedProperties.tagsForVisibility,
                styleForForm:extendedProperties.styleForForm,
                afterInsertExtraProcess:extendedProperties.afterInsertExtraProcess,
                sharedColList: extendedProperties.sharedColList
                }
            return result;
            
        else:
            return { result:"NO Extended Properties"};
        """