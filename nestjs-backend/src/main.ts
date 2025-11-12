import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // Enable CORS
  app.enableCors({
    origin: [
      'http://localhost:5173',
      'http://localhost:3000',
      'http://localhost:8000',
    ],
    credentials: true,
  });

  // Set global prefix
  app.setGlobalPrefix('api');

  await app.listen(3001);
  console.log('🚀 NestJS running on http://localhost:3001');
}
bootstrap();