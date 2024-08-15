SELECT count(*) FROM Traspasos_LIN WHERE @{WHERE} AND (Origen = 'Ensanche' OR Destino = 'Ensanche') order by @{ORDER}
