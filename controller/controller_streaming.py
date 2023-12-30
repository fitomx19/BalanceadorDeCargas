from app.services.services_streaming import StreamingService
from app.services.user_services_streaming import StreamingUserService
from app.services.suscription_services_streaming import SuscriptionService
from app.services.contents_services_streaming import ContentService
from app.services.payment_services_streaming import PaymentService
from app.services.stats_services_streaming import StatsService



#production
#from services.services_streaming import StreamingService
#from services.user_services_streaming import StreamingUserService
#from services.suscription_services_streaming import SuscriptionService
#from services.contents_services_streaming import ContentService
#from services.payment_services_streaming import PaymentService
#from services.stats_services_streaming import StatsService


class StreamingController:
    def saludar(self):
        mensaje = StreamingService.obtener_mensaje()
        return {'mensaje': mensaje}
    
    def subir_archivo_al_servidor(self):
        return StreamingService.subir_archivo_al_servidor()
    
    def obtener_archivos(self):
        return StreamingService.obtener_archivos()
    
    def obtener_archivo(self, nombre_archivo):
        return StreamingService.obtener_archivo(nombre_archivo)
    
    #Administracion de Usuarios
    def crear_usuario(self):
        return StreamingUserService.crear_usuario()
    
    def obtener_usuarios(self):
        return StreamingUserService.obtener_usuarios()
    
    def obtener_usuario(self, nombre_usuario):
        return StreamingUserService.obtener_usuario(nombre_usuario)
    
    def actualizar_usuario(self, nombre_usuario):
        return StreamingUserService.actualizar_usuario(nombre_usuario)
    
    def eliminar_usuario(self, nombre_usuario):
        return StreamingUserService.eliminar_usuario(nombre_usuario)
    
    #Suscripción e Inicio de Sesión:
    def suscripcion(self):
        return SuscriptionService.suscripcion()
    
    def login(self):
        return SuscriptionService.login()
    
    def logingGET(self):
        return SuscriptionService.loginGet()
        
    
    #Gestion de Contenidos
    def obtener_catalogo(self):
        return ContentService.obtener_catalogo()
    
    def obtener_contenido(self, nombre_contenido):
        return ContentService.obtener_contenido(nombre_contenido)
    
   # gestion de pagos

    def realizar_pago(self):
        return PaymentService.realizar_pago()
    
    def obtener_pagos(self):
        return PaymentService.obtener_pagos()
    
    def obtener_pago(self, nombre_pago):
        return PaymentService.obtener_pago(nombre_pago)
    
    def actualizar_pago(self, nombre_pago):
        return PaymentService.actualizar_pago(nombre_pago)
    
    #estadisticas
    def obtener_estadisticas(self):
        return StatsService.obtener_estadisticas()
    
