import jinja2

relationships = {
    "relationships": [
        {
        "parentEntity": "Cliente",
        "childEntity": "Ventas_LIN",
        "roleToParent": "Cliente",
        "roleToChild": "Ventas_LIN_List",
        "deleteRule": "No Action",
        "updateRule": "No Action",
        "parentColumns": [
            "NCuenta"
        ],
        "childColumns": [
            "NCuentaCliente"
        ]
        },
        {
        "parentEntity": "Compras_CAB",
        "childEntity": "Compras_LIN",
        "roleToParent": "Compras_CAB",
        "roleToChild": "Compras_LIN_List",
        "deleteRule": "No Action",
        "updateRule": "No Action",
        "parentColumns": [
            "SerieNúmero"
        ],
        "childColumns": [
            "AlbaránCompra"
        ]
        },
        {
        "parentEntity": "Producto",
        "childEntity": "Compras_LIN",
        "roleToParent": "Producto",
        "roleToChild": "Compras_LIN_List",
        "deleteRule": "No Action",
        "updateRule": "No Action",
        "parentColumns": [
            "Referencia"
        ],
        "childColumns": [
            "ReferenciaProducto"
        ]
        },
        {
        "parentEntity": "Producto",
        "childEntity": "StockTienda",
        "roleToParent": "Producto_1",
        "roleToChild": "StockTienda_List",
        "deleteRule": "No Action",
        "updateRule": "No Action",
        "parentColumns": [
            "Referencia"
        ],
        "childColumns": [
            "Referencia"
        ]
        },
        {
        "parentEntity": "Producto",
        "childEntity": "Traspasos_LIN",
        "roleToParent": "Producto_1",
        "roleToChild": "Traspasos_LIN_List",
        "deleteRule": "No Action",
        "updateRule": "No Action",
        "parentColumns": [
            "Referencia"
        ],
        "childColumns": [
            "Referencia"
        ]
        },
        {
        "parentEntity": "Producto",
        "childEntity": "Ventas_LIN",
        "roleToParent": "Producto_1",
        "roleToChild": "Ventas_LIN_List",
        "deleteRule": "No Action",
        "updateRule": "No Action",
        "parentColumns": [
            "Referencia"
        ],
        "childColumns": [
            "RefProducto"
        ]
        },
        {
        "parentEntity": "Proveedor",
        "childEntity": "Compras_CAB",
        "roleToParent": "Proveedor",
        "roleToChild": "Compras_CAB_List",
        "deleteRule": "No Action",
        "updateRule": "No Action",
        "parentColumns": [
            "NºCuenta"
        ],
        "childColumns": [
            "NºCuentaProveedor"
        ]
        },
        {
        "parentEntity": "Proveedor",
        "childEntity": "Compras_LIN",
        "roleToParent": "Proveedor",
        "roleToChild": "Compras_LIN_List",
        "deleteRule": "No Action",
        "updateRule": "No Action",
        "parentColumns": [
            "NºCuenta"
        ],
        "childColumns": [
            "NºCuentaProveedor"
        ]
        },
        {
        "parentEntity": "StockTienda",
        "childEntity": "Compras_LIN",
        "roleToParent": "StockTienda",
        "roleToChild": "Compras_LIN_List",
        "deleteRule": "No Action",
        "updateRule": "No Action",
        "parentColumns": [
            "idTienda",
            "Referencia"
        ],
        "childColumns": [
            "idTienda",
            "ReferenciaProducto"
        ]
        },
        {
        "parentEntity": "StockTienda",
        "childEntity": "Traspasos_LIN",
        "roleToParent": "StockTienda",
        "roleToChild": "Traspasos_LIN_List_DESTINO",
        "deleteRule": "No Action",
        "updateRule": "No Action",
        "parentColumns": [
            "Referencia",
            "Tienda"
        ],
        "childColumns": [
            "Referencia",
            "Destino"
        ]
        },
        {
        "parentEntity": "StockTienda",
        "childEntity": "Traspasos_LIN",
        "roleToParent": "StockTienda_1",
        "roleToChild": "Traspasos_LIN_List_ORIGEN",
        "deleteRule": "No Action",
        "updateRule": "No Action",
        "parentColumns": [
            "Referencia",
            "Tienda"
        ],
        "childColumns": [
            "Referencia",
            "Origen"
        ]
        },
        {
        "parentEntity": "StockTienda",
        "childEntity": "Ventas_LIN",
        "roleToParent": "StockTienda",
        "roleToChild": "Ventas_LIN_List",
        "deleteRule": "No Action",
        "updateRule": "No Action",
        "parentColumns": [
            "Referencia",
            "Tienda"
        ],
        "childColumns": [
            "RefProducto",
            "Tienda"
        ]
        },
        {
        "parentEntity": "Ventas_CAB",
        "childEntity": "Ventas_LIN",
        "roleToParent": "Ventas_CAB",
        "roleToChild": "Ventas_LIN_List",
        "deleteRule": "No Action",
        "updateRule": "No Action",
        "parentColumns": [
            "Número"
        ],
        "childColumns": [
            "Número"
        ]
        }
    ]
    }
    
def generate_relns(rel):
    '''
    models.ComprasLIN.Compras_CAB = relationship("ComprasCAB",
    cascade_backrefs=False, backref='Compras_LIN_List',
    primaryjoin = remote(models.ComprasCAB.SerieNmero) == foreign(models.ComprasLIN.AlbarnCompra))
    {
        "parentEntity": "Compras_CAB",
        "childEntity": "Compras_LIN",
        "roleToParent": "Compras_CAB",
        "roleToChild": "Compras_LIN_List",
        "deleteRule": "No Action",
        "updateRule": "No Action",
        "parentColumns": [
            "SerieNúmero"
        ],
        "childColumns": [
            "AlbaránCompra"
        ]
        },
    '''
    roleToParent =rel['roleToParent']
    roleToChild = rel['roleToChild']
    parentEntity = rel['parentEntity'].replace("_", "",1)
    parentColumns = rel['parentColumns'][0]
    childEntity  = rel['childEntity'].replace("_", "",1)
    childColumns =   rel['childColumns'][0]
    parent_key_template = jinja2.Template("{{parent_table}}.{{parent_attr}}")
    child_key_template = jinja2.Template("{{child_table}}.{{child_attr}}")
    reln_template = jinja2.Template("models.{{childEntity}}.{{roleToParent}} = relationship('{{parentEntity}}', \n backref='{{roleToChild}}', \n primaryjoin=remote(models.{{parentEntity}}.{{parentColumns}}) == foreign(models.{{childEntity}}.{{childColumns}}))\n")
    print(reln_template.render(childEntity=childEntity, roleToParent=roleToParent, roleToChild=roleToChild, parentEntity=parentEntity, childColumns=childColumns, parentColumns=parentColumns))
    '''
    parent_fkey = jinja2.Template("ForeignKey('{{parent_table}}.{{parent_attr}}'),")
    parent_reln = jinja2.Template("{{roleToParent}} :Mapped['{{parent_table}}'] = relationship('{{parent_table}}', backref='{{child_table}}')\n")
    child_reln = jinja2.Template("{{roleToChild}} :Mapped['{{child_table}}'] = relationship('{{parent_table}}', backref='{{child_table}}')\n")
    
    #parent_reln2 = jinja2.Template("    primaryjoin=remote('{{parent_table}}.{{parent_attr}}') == foreign('{{child_table}}.{{child_attr}}'))")  
    print (parent_fkey.render(parent_table=parent_table, parent_attr=parent_attr))
    print(parent_reln.render(roleToParent=roleToParent,parent_table=parent_table, child_table=child_table))
    '''
    pass

if __name__ == "__main__":
    for rel in relationships['relationships']:
        generate_relns(rel)
    