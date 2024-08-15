//log.debug(logicContext.getLogicNestLevel() + 'row.StockTienda.FechaInventario > row.FechaAlbarán '+ row.StockTienda.FechaInventario  + " "+ row.FechaAlbarán);
if (row.StockTienda && logicContext.getLogicNestLevel()=== 0)
    {
        if (row.StockTienda.FechaInventario > row.FechaAlbarán )
            return false;
        else
            return true;
    }
    return true;
