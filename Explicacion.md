La clean arquitecture se basa en 3 principios.

1. Independencia total
Esto aplicado se entiende de la siguiente manera: El codigo de negocio no sabe ni le importa si los datos vienen de 
una base de datos SQL, una API o archivo de texto. Solo cumple con su mision sin cuestionar como le llegan los datos.

2. La regla de la dependencia
Esto se puede ver en las dependencias, las cuales siempre apuntan hacia el centro. Las capas exteriores pueden conocer
las del interior, pero no al reves.

3. Separacion por capas
Esta es mas evidente que las otras, aqui de o un ejemplo:

Entidades ==> Son las reglas globales.
Casos de Uso ==> Reglas especificas para funciones concretas.
Adaptadores e infraestructura ==> Conectores con por ejemplo una base de datos o un servidor web.

---

## 2. Estructura de Directorios

```text
src/
├── domain/                # Capa 1: El Corazón (Lógica pura)
│   ├── entities/          # Objetos de negocio (ej. User.ts)
│   ├── repositories/      # Contratos/Interfaces (ej. UserRepository.ts)
│   └── value-objects/     # Objetos sin identidad propia
├── application/           # Capa 2: Casos de Uso
│   ├── use-cases/         # Lógica de aplicación (ej. CreateUser.ts)
│   └── dtos/              # Estructuras de datos de entrada/salida
├── infrastructure/        # Capa 3: Detalles Técnicos
│   ├── repositories/      # Implementaciones (ej. MongoUserRepository.ts)
│   ├── external-services/ # Clientes de terceros
│   └── persistence/       # Configuración de ORMs/Drivers
└── presentation/          # Capa 4: Entrada y Salida
    ├── controllers/       # Manejadores de rutas
    ├── routes/            # Definición de endpoints
    └── middlewares/       # Lógica de pre-procesamiento