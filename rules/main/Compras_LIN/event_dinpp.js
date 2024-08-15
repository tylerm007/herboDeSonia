log.debug('>>>>>>>>>>>>>>>>>> Event: PonStockIncial >>>>>>>>>>>>>>>>>>')
 if ((logicContext.getInitialVerb() == "UPDATE" || logicContext.getInitialVerb() == "INSERT") && row.FechaAlbarán >= row.FechaInventario) 
 {
  parentRow = row.StockTienda;
  log.debug(row.Cantidad+ " logicContext.getLogicNestLevel() "+ logicContext.getLogicNestLevel());
    if (parentRow && logicContext.getLogicNestLevel() === 0)
    {
        log.debug(' TIENE PADRE ' + parentRow);
        if (row.NºCuentaProveedor === 0)
        {
            log.debug(' es el proveedor Inventario ' + parentRow);
            logicContext.touch(parentRow);
            parentRow.StockInicial = row.Cantidad;
            parentRow.FechaInventario = row.FechaAlbarán;
            if (logicContext.getInitialVerb() == "INSERT")
                {
                parentRow.Entradas = 0;
                parentRow.Salidas = 0;
                } 
            logicContext.update(parentRow);
        }
    }
 }    
