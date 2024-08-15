resourceName=req.urlParameters.filter+"";
var extendedProperties = listenerUtil.getExtendedPropertiesFor
("v1", resourceName);
if (extendedProperties)// && extendedProperties.MyExtension) {
{
var result = {
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
    sharedColList:extendedProperties.sharedColList
};
return result;
}
else 
{
    return { result:"NO Extended Properties"};
}
