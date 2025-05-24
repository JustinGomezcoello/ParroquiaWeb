
from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages  # si vas a mostrar mensajes


def registrar_catequizando(request):
    mensaje = ""
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        fechanacimiento = request.POST.get('fechanacimiento')
        parroquia = request.POST.get('parroquiaorigen')
        estado = request.POST.get('estado')
        tienefe = 1 if request.POST.get('tienefebautismo') == 'on' else 0
        observaciones = request.POST.get('observaciones')

        with connection.cursor() as cursor:
            try:
                cursor.execute("""
                    EXEC sp_RegistrarCatequizando 
                        @nombres=%s, @apellidos=%s, @fechanacimiento=%s, 
                        @parroquiaorigen=%s, @estado=%s, 
                        @tienefebautismo=%s, @observaciones=%s
                """, [nombres, apellidos, fechanacimiento, parroquia, estado, tienefe, observaciones])
                mensaje = "✅ Catequizando registrado correctamente"
            except Exception as e:
                mensaje = f"❌ Error: {str(e)}"

    return render(request, 'catequesis/registrar_catequizando.html', {'mensaje': mensaje})

def listar_catequizandos(request):
    resultado = []
    mensaje = ""

    if request.method == 'POST':
        idcatequista = request.POST.get('idcatequista')

        with connection.cursor() as cursor:
            try:
                cursor.execute("EXEC sp_ListarCatequizandoPorCatequista @idcatequista=%s", [idcatequista])
                rows = cursor.fetchall()
                resultado = [
                    {'id': row[0], 'nombres': row[1], 'apellidos': row[2], 'estado': row[3], 'parroquia': row[4]}
                    for row in rows
                ]
                mensaje = "✅ Resultados encontrados"
            except Exception as e:
                mensaje = f"❌ Error: {str(e)}"

    return render(request, 'catequesis/listar_catequizandos.html', {'resultado': resultado, 'mensaje': mensaje})


def home(request):
    return render(request, 'catequesis/home.html')

def listar_todos_catequizandos(request):
    resultado = []
    mensaje = ""

    with connection.cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM registro.catequizado")
            rows = cursor.fetchall()
            resultado = [
                {
                    'id': row[0], 'nombres': row[1], 'apellidos': row[2],
                    'fechanacimiento': row[3], 'parroquia': row[4],
                    'estado': row[5], 'tienefebautismo': row[6], 'observaciones': row[7]
                }
                for row in rows
            ]
            mensaje = "✅ Catequizandos cargados"
        except Exception as e:
            mensaje = f"❌ Error: {str(e)}"

    return render(request, 'catequesis/listar_todos_catequizandos.html', {
        'resultado': resultado,
        'mensaje': mensaje
    })


def modificar_catequizando(request, id):
    mensaje = ""
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        fechanacimiento = request.POST.get('fechanacimiento')  # <-- AÑADIDO
        parroquia = request.POST.get('parroquiaorigen')
        estado = request.POST.get('estado')
        tienefe = 1 if request.POST.get('tienefebautismo') == 'on' else 0
        observaciones = request.POST.get('observaciones')

        with connection.cursor() as cursor:
            try:
                cursor.execute("""
                    EXEC sp_ModificarCatequizando 
                        @idcatequizado=%s, @nombres=%s, @apellidos=%s, @fechanacimiento=%s,
                        @parroquiaorigen=%s, @estado=%s, @tienefebautismo=%s, @observaciones=%s
                """, [id, nombres, apellidos, fechanacimiento,
                      parroquia, estado, tienefe, observaciones])
                mensaje = "✅ Catequizando modificado"
                return redirect('catequesis:listar_todos_catequizandos')
            except Exception as e:
                mensaje = f"❌ Error: {str(e)}"

    # GET: Cargar datos existentes
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM registro.catequizado WHERE idcatequizado = %s", [id])
        row = cursor.fetchone()

    return render(request, 'catequesis/modificar_catequizando.html', {
        'mensaje': mensaje,
        'catequizando': row
    })




def eliminar_catequizando(request, id):
    mensaje = ""
    with connection.cursor() as cursor:
        try:
            cursor.execute("EXEC sp_EliminarCatequizando @idcatequizado=%s", (id,))
            mensaje = "✅ Catequizando eliminado"
        except Exception as e:
            mensaje = f"❌ Error al eliminar: {str(e)}"
    
    return redirect('catequesis:listar_todos_catequizandos')





#CRUD CATEQUISTAS
def listar_catequistas(request):
    resultado = []
    mensaje = ""
    with connection.cursor() as cursor:
        try:
            cursor.execute("EXEC sp_ListarCatequistas")
            rows = cursor.fetchall()
            resultado = rows
            mensaje = "✅ Catequistas cargados"
        except Exception as e:
            mensaje = f"❌ Error: {str(e)}"
    return render(request, 'catequesis/listar_catequistas.html', {'resultado': resultado, 'mensaje': mensaje})


def registrar_catequista(request):
    mensaje = ""
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        rol = request.POST.get('rol')
        nivel = request.POST.get('nivel') or None

        try:
            if nivel:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT COUNT(*) FROM registro.nivelcatequesis WHERE idnivelcatequesis = %s", [nivel])
                    count = cursor.fetchone()[0]
                    if count == 0:
                        mensaje = f"❌ El nivel con ID {nivel} no existe. Ingresa un valor válido entre 1 y 2"
                        return render(request, 'catequesis/registrar_catequista.html', {'mensaje': mensaje})

            with connection.cursor() as cursor:
                cursor.execute("""
                    EXEC sp_RegistrarCatequista @nombres=%s, @apellidos=%s, @telefono=%s, @correo=%s, @rol=%s, @nivel=%s
                """, [nombres, apellidos, telefono, correo, rol, nivel])
                mensaje = "✅ Catequista registrado correctamente"
        except Exception as e:
            mensaje = f"❌ Error: {str(e)}"

    return render(request, 'catequesis/registrar_catequista.html', {'mensaje': mensaje})



def modificar_catequista(request, id):
    mensaje = ""
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        rol = request.POST.get('rol')
        nivel = request.POST.get('nivel') or None

        with connection.cursor() as cursor:
            try:
                cursor.execute("""
                    EXEC sp_ModificarCatequista @id=%s, @nombres=%s, @apellidos=%s, @telefono=%s, @correo=%s, @rol=%s, @nivel=%s
                """, [id, nombres, apellidos, telefono, correo, rol, nivel])
                return redirect('catequesis:listar_catequistas')
            except Exception as e:
                mensaje = f"❌ Error: {str(e)}"

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM registro.catequista WHERE idcatequista = %s", [id])
        row = cursor.fetchone()

    return render(request, 'catequesis/modificar_catequista.html', {'catequista': row, 'mensaje': mensaje})


def eliminar_catequista(request, id):
    with connection.cursor() as cursor:
        try:
            # Primero intenta eliminar SIN forzar
            cursor.execute("EXEC sp_EliminarCatequista @id=%s, @forzar=0", [id])
        except Exception as e:
            error_msg = str(e)
            if 'No se puede eliminar el catequista' in error_msg:
                # Extraer el número de asignaciones del mensaje
                asignaciones = error_msg.split('tiene ')[1].split(' asignaciones')[0]
                # Mostrar mensaje de confirmación
                return render(request, 'catequesis/confirmar_eliminar_catequista.html', {
                    'id': id,
                    'asignaciones': asignaciones,
                    'mensaje': 'El catequista tiene asignaciones. ¿Deseas eliminarlas también en cascada?'
                })
            else:
                print(f"❌ Error al eliminar: {error_msg}")
    return redirect('catequesis:listar_catequistas')


def eliminar_catequista_confirmado(request, id):
    with connection.cursor() as cursor:
        try:
            cursor.execute("EXEC sp_EliminarCatequista @id=%s, @forzar=1", [id])
        except Exception as e:
            print(f"❌ Error al eliminar (forzado): {str(e)}")
    return redirect('catequesis:listar_catequistas')
