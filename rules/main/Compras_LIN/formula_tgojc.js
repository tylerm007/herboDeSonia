var dto1 = (100 - row.tpcDescuento1) / 100;
var dto2 = (100 - row.tpcDescuento2) / 100;
var importe = row.CantidadConCoste * row.PrecioCoste;
importe = importe * dto1;
importe = importe * dto2;
return importe;
