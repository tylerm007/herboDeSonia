row.cabLin1 = "RACRISSON S.L. - HERBOLARIO";
row.cabLin2 = "SONIA";
row.cabLin3 = "AVDA PABLO NERUDA 91-97";
row.cabLin4 = row.Tienda;
row.cabLin5 = " ";
row.cabLin6 = "CIF:B87472486";
row.cabLin7 = "Código del cliente:" + row.NCuentaCliente;
row.cabLin8 = "Factura simplif. " + row.VentaMostrador;
row.fecha = row.FechaVenta;
row.footerLin1 = "IVA";
var space = "                      ";
var lineasIvas = "";

if (row.BaseIVACero !== 0) {
    row.footerLin2 = space + "0 x " + row.BaseIVACero.toFixed(2) + "    " + "0,00";
    lineasIvas += ",footerLin2";
}

if (row.BaseIVASuperReducido !== 0) {
    row.footerLin3 = space + "4 x " + row.BaseIVASuperReducido.toFixed(2) + "    " + row.ImporteIVASuperReducido.toFixed(2);
    lineasIvas += ",footerLin3";
}

if (row.BaseIVAAceitesPastas !== 0) {
    row.footerLin4 = space + "5 x " + row.BaseIVAAceitesPastas.toFixed(2) + "    " + row.ImporteIVAAceitesPastas.toFixed(2);
    lineasIvas += ",footerLin4";
}

if (row.BaseIVAReducido !== 0) {
    row.footerLin5 = space + "10 x " + row.BaseIVAReducido.toFixed(2) + "    " + row.ImporteIVAReducido.toFixed(2);
    lineasIvas += ",footerLin5";
}

if (row.BaseIVAGeneral !== 0) {
    row.footerLin6 = space + "21 x " + row.BaseIVAGeneral.toFixed(2) + "    " + row.ImporteIVAGeneral.toFixed(2);
    lineasIvas += ",footerLin6";
}

lineasIvas = lineasIvas.substring(1); // elimina la coma inicial


row.footerLin7 = "TOTAL                              " + row.ImporteTotal.toFixed(2);

row.MapPrintFields='#CAB#cabLin1,cabLin2,cabLin3,cabLin4,cabLin5,cabLin6,cabLin7,fecha,cabLin7#LIN#List-Ventas_LIN#HEADER#PROD/SERV     UND/H               TOTAL#L1#Producto#L2#SPACE(15),CantidadXPrecio,ImporteBruto#sizes#46,15,20,15#FOOT#footerLin1,'+lineasIvas+',footerLin7';
