var dtoProntoPago = (100 - row.tpcDtoProntoPago) / 100;
var dtoGlobal = (100 - row.tpcDtoGlobal) / 100;
var baseIVASuperReducido = row.BaseIVASuperReducido * dtoProntoPago;
baseIVASuperReducido = baseIVASuperReducido * dtoGlobal;

return baseIVASuperReducido * 4 /100;
