class Estudiar:

    def __init__(self):
        pass

    def rutina_diaria(self, descanso = 'poco'):
        self._despertar()
        self._comer()
        self._universidad()
        self._libre(descanso)

    def _despertar(self):
        print('despertar temprano')

    def _comer(self):
        print('alimentarse')

    def _universidad(self):
        print('estudiar online')

    def _libre(self, descanso):
        if descanso == 'poco':
            print('seguir estudiando')
        else:
            print('descansar')

if __name__ == '__main__':
    estudiar = Estudiar()
    estudiar.rutina_diaria()