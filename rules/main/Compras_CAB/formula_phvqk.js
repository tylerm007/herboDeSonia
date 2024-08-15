var dtoProntoPago = (100 - row.tpcDtoProntoPago) / 100;
var dtoGlobal = (100 - row.tpcDtoGlobal) / 100;

var baseIVAGeneral = row.BaseIVAGeneral * dtoProntoPago;
baseIVAGeneral = baseIVAGeneral * dtoGlobal;

var baseIVAReducido = row.BaseIVAReducido * dtoProntoPago;
baseIVAReducido = baseIVAReducido * dtoGlobal;

var baseIVAAceitesPastas = row.BaseIVAAceitesPastas * dtoProntoPago;
baseIVAAceitesPastas = baseIVAAceitesPastas * dtoGlobal;

var baseIVASuperReducido = row.BaseIVASuperReducido * dtoProntoPago;
baseIVASuperReducido = baseIVASuperReducido * dtoGlobal;

var baseIVACero = row.BaseIVACero * dtoProntoPago;
baseIVACero = baseIVACero * dtoGlobal;

return baseIVAGeneral + baseIVAReducido + baseIVAAceitesPastas + baseIVASuperReducido + baseIVACero;
