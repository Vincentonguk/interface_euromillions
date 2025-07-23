import subprocess

def run_cmd(cmd):
    print(f"\nPronto pra rodar: {cmd}")
    confirm = input("Quer rodar agora? (s/n): ").lower()
    if confirm == "s":
        result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
        print(result.stdout)
        if result.stderr:
            print("⚠️ Erro:", result.stderr)
    else:
        print("🚫 Pulando comando.")

print("🤖 SelfBot 2.0 ligado!")
print("Diga o que você quer fazer hoje:")

task = input("> ")

if "deploy" in task.lower():
    print("\nOk, vou rodar os comandos pra deploy no GitHub.\n")

    # Ver status do Git
    run_cmd('git status')

    # Adiciona automaticamente TODOS os arquivos modificados
    run_cmd('git add .')

    # Commit com mensagem
    commit_msg = input("\nEscreva a mensagem do commit (ou pressione Enter para usar 'deploy by SelfBot'):\n> ")
    if not commit_msg.strip():
        commit_msg = "deploy by SelfBot"
    run_cmd(f'git commit -m "{commit_msg}"')

    # Push
    run_cmd('git push')

else:
    print("🚧 Ainda não sei como ajudar nessa tarefa, mas posso aprender!")

print("\n✅ SelfBot terminou sua missão. Até mais, mestre!")
