# ========== PYTHON ==========
# 1. Criação do dicionário
usuario = {
    "login": "ana_silva",
    "status": "Inativo",
    "nivel": "Editor"
}
# 2. Uso do .get() para verificar se uma chave existe
# Se não existir, retorna o valor padrão "Não informado“
email = usuario.get("email", "Não informado")
print(f"E-mail do usuário: {email}")
# Saída: Não informado
# 3. Uso do .update() para atualizar dados e adicionar novos campos
usuario.update({
    "status": "Ativo",
    # Modifica o status existente
    "email": "ana@email.com"  # Adiciona uma nova chave
})

''' 
========== PORTUGOL ==========

programa 
{
// 1. Criação da estrutura base
tipo tipo_usuário
{
    cadeia login
    cadeia status
    cadeia nível
    cadeia email
    
    // Variáveis de controle para simular se o campo existe (Python dinâmico) 
    
    logico tem_email
    logico tem_nível
}
'''