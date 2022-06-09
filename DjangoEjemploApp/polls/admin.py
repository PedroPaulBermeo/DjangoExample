from django.contrib import admin
from .models import Question, Choice

#Me va a servir para colocar respuesta al momento de crear las preguntas
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3 #Digo que para cada pregunta yo voy a tener la opcion de generar
              #por lo menos 3 respuestas por defecto

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"] #Me permite generar el orden en el que quiero ver los campos en el admin
    inlines = [ChoiceInline]#Asocio a las respuestas
    list_display = ("question_text", "pub_date", "was_published_recently")#Esto es para afectar como se ve la lista del modelo que estamos editando,
                                                                  #en este caso la lista de preguntas
    list_filter = ["pub_date"] #dependiendo del tipo de dato que le coloque, puedo filtrar ese dato
    search_fields = ["question_text"]#Cuadro de Busqueda

admin.site.register(Question, QuestionAdmin) #Se debe registrar los modelos en el Admin que realice
