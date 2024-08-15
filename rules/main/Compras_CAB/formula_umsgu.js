var dtoProntoPago = (100 - row.tpcDtoProntoPago) / 100;
var dtoGlobal = (100 - row.tpcDtoGlobal) / 100;
var baseIVAAceitesPastas = row.BaseIVAAceitesPastas * dtoProntoPago;
baseIVAAceitesPastas = baseIVAAceitesPastas * dtoGlobal;
return baseIVAAceitesPastas * 5 /100;
