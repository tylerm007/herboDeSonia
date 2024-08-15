SELECT count(*) FROM Traspasos_LIN WHERE @{WHERE} AND (Origen = 'Centro Comercial' OR Destino = 'Centro Comercial') order by @{ORDER}
