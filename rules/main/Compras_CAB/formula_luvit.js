var dtoProntoPago = (100 - row.tpcDtoProntoPago) / 100;
var dtoGlobal = (100 - row.tpcDtoGlobal) / 100;
log.debug('dtoProntoPago '+  dtoProntoPago + ' dtoGlobal '+ dtoGlobal);
var baseIVAReducido = row.BaseIVAReducido * dtoProntoPago;
log.debug('row.baseIVAReducido '+ row.baseIVAReducido + ' baseIVAReducido '+ baseIVAReducido);
baseIVAReducido = baseIVAReducido * dtoGlobal;
log.debug(' baseIVAReducido ' + baseIVAReducido);
return baseIVAReducido * 10 /100;
