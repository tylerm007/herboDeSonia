log.debug('>>>>>>>>>>>>>>>>>> Event: keepLastPVP >>>>>>>>>>>>>>>>>>')
 if ((logicContext.getInitialVerb() == "UPDATE" && row.PVPProducto != oldRow.PVPProducto) || logicContext.getInitialVerb() == "INSERT") 
 {
  parentRow = row.Producto;
  log.debug(row.Cantidad+ " logicContext.getLogicNestLevel() "+ logicContext.getLogicNestLevel());
    if (parentRow && logicContext.getLogicNestLevel() === 0)
    {
        log.debug(' TIENE PADRE ' + parentRow);
        if (parentRow.FechaUltPVP === null || ( row.FechaAlbarán >= parentRow.FechaUltPVP))
        {
            log.debug(' la fecha de Ult PVP ' + row.Producto.FechaUltPVP);
            logicContext.touch(parentRow);
            parentRow.FechaUltPVP = row.FechaAlbarán;
            parentRow.PVP = row.PVPProducto;
            logicContext.update(parentRow);
        }
    }
 }    
