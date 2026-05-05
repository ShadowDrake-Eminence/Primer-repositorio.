// src/presentation/controllers/UserController.ts
// Controlador que recibe datos de la capa de presentación y llama al caso de uso.
// import { CreateUser } from '../../application/use-cases/CreateUser'
// import { UserPresenter } from '../presenters/UserPresenter'
// import { validateUserPayload } from '../middlewares/ValidateUserPayload'

// export class UserController {
//   constructor(private createUser: CreateUser) {}

//   async handle(requestBody: any): Promise<object> {
//     validateUserPayload(requestBody)

//     const result = await this.createUser.execute({
//       name: requestBody.name,
//       email: requestBody.email
//     })

//     return UserPresenter.format(result)
//   }
// }
