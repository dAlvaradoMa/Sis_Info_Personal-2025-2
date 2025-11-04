AWSTemplateFormatVersion: '2010-09-09'
Description: "Ejemplo de función AWS Lambda"

Resources:
  MiFuncionLambda:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName: MiFuncionLambda
      Runtime: python3.13
      Handler: index.lambda_handler
      Role: arn:aws:iam::123456789012:role/LambdaExecutionRole
      #Esto le da permisos a la función para ejecutarse (por ejemplo, escribir logs en CloudWatch).
      Timeout: 10
      MemorySize: 128

'''Runtime → usa Python 3.12.
Handler → le dice a Lambda que ejecute la función lambda_handler dentro del archivo index.py.
Timeout: 10 → la función puede ejecutarse hasta 10 segundos antes de que AWS la detenga.
MemorySize: 128 → asigna 128 MB de RAM (lo mínimo, para funciones ligeras).
'''
      Code:
        ZipFile: |
          import json

          def lambda_handler(event, context):
              return {
                  'statusCode': 200,
                  'body': json.dumps('¡Hola desde Lambda!')
              }

#El bloque ZipFile contiene el código Python inline (es decir, el código se guarda dentro de la plantilla CloudFormation, sin necesidad de un archivo ZIP externo).

Outputs:
  LambdaARN:
    Description: ARN de la función Lambda creada
    Value: !GetAtt MiFuncionLambda.Arn

#Esto hace que, al terminar la creación del stack, CloudFormation te muestre el ARN de la función (su identificador único en AWS).