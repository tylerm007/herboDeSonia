SELECT count(*) FROM Traspasos_LIN WHERE @{WHERE} AND (Origen = 'RIVAS VACIAMADRID' OR Destino = 'RIVAS VACIAMADRID') order by @{ORDER}
