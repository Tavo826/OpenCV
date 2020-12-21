#Representación en opencv
#[next, Previous, First_Child, Parent]
# -Next: siguiente contorno en el mismo nivel de jerarquía
# -Previous: Contorno anterior en el mismo nivel de jerarquía
# -First_Child: primer hijo del contorno
# -Parent: padre del contorno

#MODE

# RETR_LIST: recupera todos los contornos sin establecer jerarquía
# RETR_EXTERNAL: recupera contornos externos solamente (1 nivel de jerarquía)
# RETR_CCOMP: organiza los contornos en jerarquía de 2 niveles 
# RETR_TREE: recupera todos llos contornos con sus jerarquías