// src/presentation/App.ts
// Ejemplo de composición de dependencias en la capa de entrada.
// import { FakeUserRepository } from '../infrastructure/repositories/FakeUserRepository'
// import { ConsoleLogger } from '../infrastructure/external-services/ConsoleLogger'
// import { ConsoleEmailService } from '../infrastructure/external-services/ConsoleEmailService'
// import { CreateUser } from '../application/use-cases/CreateUser'
// import { UserController } from './controllers/UserController'
// import { UserRoutes } from './routes/UserRoutes'

// const repository = new FakeUserRepository()
// const logger = new ConsoleLogger()
// const emailService = new ConsoleEmailService(logger)
// const createUser = new CreateUser(repository, emailService)
// const userController = new UserController(createUser)
// const userRoutes = new UserRoutes(userController)

// userRoutes.register()

// // Ejemplo de uso
// userRoutes.createUser({ name: 'Ana Pérez', email: 'ana@example.com' })
