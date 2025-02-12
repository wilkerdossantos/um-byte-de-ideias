# Um Byte de Ideias

**Um Byte de Ideias** é um blog desenvolvido utilizando o framework Django. O projeto tem como objetivo compartilhar conteúdos sobre desenvolvimento de software, tecnologia e ideias inovadoras.

## Tecnologias Utilizadas

- **Django**: Framework web utilizado para o desenvolvimento do blog.
- **Python**: Linguagem de programação usada no backend.
- **HTML/CSS/JavaScript**: Para a construção do frontend.
- **SQLite**: Banco de dados padrão para o desenvolvimento (pode ser configurado para usar outros DBs, como PostgreSQL).

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/wilkerdossantos/um-byte-de-ideias.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd um-byte-de-ideias
   ```

3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use venv\Scripts\activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

6. Crie um superusuário para acessar o admin:
   ```bash
   python manage.py createsuperuser
   ```

7. Execute o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

8. Acesse o blog em [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Contribuindo

1. Faça um fork deste repositório.
2. Crie uma nova branch (`git checkout -b minha-contribuicao`).
3. Faça suas alterações e commite-as (`git commit -am 'Adicionando minha contribuição'`).
4. Envie para o repositório remoto (`git push origin minha-contribuicao`).
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
