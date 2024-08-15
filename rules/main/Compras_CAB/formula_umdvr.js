var dtoProntoPago = (100 - row.tpcDtoProntoPago) / 100;
var dtoGlobal = (100 - row.tpcDtoGlobal) / 100;
var baseIVAGeneral = row.BaseIVAGeneral * dtoProntoPago;
baseIVAGeneral = baseIVAGeneral * dtoGlobal;
return baseIVAGeneral *21 /100;
