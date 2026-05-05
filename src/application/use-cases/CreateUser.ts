// src/application/use-cases/CreateUser.ts
// Caso de uso que crea un usuario y delega persistencia y notificaciones.
//import { CreateUserDTO } from '../dtos/CreateUserDTO'
//import { UserResponseDTO } from '../dtos/UserResponseDTO'
//import { UserRepository } from '../../domain/repositories/UserRepository'
//import { User } from '../../domain/entities/User'
//import { Email } from '../../domain/value-objects/Email'
//import { EmailService } from '../interfaces/EmailService'

//export class CreateUser {
  ///constructor(
    //private userRepository: UserRepository,
    //private emailService: EmailService
  //) {}

  //async execute(input: CreateUserDTO): Promise<UserResponseDTO> {
    //const email = new Email(input.email)
    //if (!email.isValid()) {
      //throw new Error('Correo inválido')
    //}

    //const alreadyExists = await this.userRepository.findByEmail(input.email)
    //if (alreadyExists) {
      //throw new Error('Usuario ya existe')
    //}

    //const user = new User(
      //String(Date.now()),
      //input.name.trim(),
      //input.email.trim()
    //)

    //await this.userRepository.save(user)
    //await this.emailService.sendWelcomeEmail(user.email, user.name)

    //return {
      //id: user.id,
      //name: user.name,
      //email: user.email
    //}
  //}
//}
