#!/bin/bash

CONF_FILE=".config"

is_installed() {
    pip show "$1" &> /dev/null
    return $?
}

install_dependencies_pip() {
    while IFS= read -r line || [[ -n "$line" ]]; do
        # Ignorar linhas vazias e comentários
        [[ -z "$line" || "$line" == \#* ]] && continue

        # Extrair o nome do módulo
        module=$(echo $line | sed 's/[<>=].*//')
        if ! is_installed $module; then
            echo "$module não está instalado. Instalando $module..."
            if pip install $line; then
                echo "$module instalado com sucesso."
            else
                echo "Falha ao instalar $module. Encerrando."
                exit 1
            fi
        fi
    done < requirements.txt
}

install_dependencies_poetry() {
    if ! [ -f pyproject.toml ]; then
        echo "pyproject.toml não encontrado. Por favor, assegure que você está no diretório correto."
        exit 1
    fi

    # Instalar dependências usando Poetry
    poetry install
}

create_conf_file() {
    local using_poetry=$1
    cat <<EOL > $CONF_FILE
dependencies_already_installed=true
using_poetry=$using_poetry
EOL
}

# Verificar se o arquivo de configuração existe e ler seus valores
if [ -f $CONF_FILE ]; then
    source $CONF_FILE
else
    dependencies_already_installed=false
    using_poetry=false

    # Perguntar ao usuário se deseja usar o Poetry
    read -p "Quer usar Poetry como package manager? (s/n): " response
    if [[ "$response" == "s" ]]; then
        if command -v poetry &> /dev/null; then
            using_poetry=true
        else
            echo "Você não tem Poetry instalado. Por favor, instale, e tente novamente."
            exit 1
        fi
    fi
fi

# Instalar dependências se ainda não estiverem instaladas
if [ "$dependencies_already_installed" != "true" ]; then
    if [ "$using_poetry" == "true" ]; then
        echo "Instalando as dependências com Poetry..."
        install_dependencies_poetry
        create_conf_file true
    else
        echo "Instalando as dependências com pip..."
        install_dependencies_pip
        create_conf_file false
    fi
fi

# Executar o script principal
if [ "$using_poetry" == "true" ]; then
    poetry run python3 main.py
else
    python3 main.py
fi
