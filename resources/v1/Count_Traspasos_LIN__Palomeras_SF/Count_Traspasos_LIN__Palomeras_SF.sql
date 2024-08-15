SELECT count(*) FROM Traspasos_LIN WHERE @{WHERE} AND (Origen = 'Palomeras' OR Destino = 'Palomeras') order by @{ORDER}
