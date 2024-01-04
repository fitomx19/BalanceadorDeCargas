from flask import Flask, request, jsonify,render_template
from repository.repository_streaming import StatsRepository 

import json
class StatsService:
    @staticmethod
    def obtener_estadisticas():
         
        estadisticas = StatsRepository.obtener_estadisticas()
         
        return render_template('estadisticas.html', estadisticas=estadisticas)
    