from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.nome
    class Meta: #Definindo o nome da classe no plural
        verbose_name_plural = "Categorias"




class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.CharField(max_length=300)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.nome
    class Meta: #Definindo o nome da classe no plural
        verbose_name_plural = "Projetos"


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    assunto = models.CharField(max_length=100)
    texto = models.TextField()
    def __str__(self) -> str:
        return 'Mensagem de '+self.nome
    class Meta: #Definindo o nome da classe no plural
        verbose_name_plural = "Contatos"


    

