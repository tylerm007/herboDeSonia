SELECT count(*) FROM Traspasos_LIN WHERE @{WHERE} AND (Origen = 'Santa Eugenia' OR Destino = 'Santa Eugenia') order by @{ORDER}
