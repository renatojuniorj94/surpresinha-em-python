clientes_produto_x = {'c1', 'c2', 'c3', 'c4', 'c5', 'c6'}
clientes_produto_y = {'c4', 'c5', 'c7', 'c8'}

interseção = clientes_produto_x & clientes_produto_y
apenas_x = clientes_produto_x - clientes_produto_y
apenas_y = clientes_produto_y - clientes_produto_x
todos_clientes = clientes_produto_x | clientes_produto_y
