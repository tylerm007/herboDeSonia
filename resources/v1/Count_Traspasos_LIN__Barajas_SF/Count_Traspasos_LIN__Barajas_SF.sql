SELECT count(*) FROM Traspasos_LIN WHERE @{WHERE} AND (Origen = 'Barajas' OR Destino = 'Barajas') order by @{ORDER}
