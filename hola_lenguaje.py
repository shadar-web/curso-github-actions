import os

def main():
    nombre = os.getenv("USERNAME", "Usuario")
    lenguaje = os.getenv("LANGUAGE", "Python")

    print("🚀 Ejecución manual del workflow")
    print(f"👤 Nombre: {nombre}")
    print(f"💻 Lenguaje favorito: {lenguaje}")

    if lenguaje == "Python":
        print("🐍 Python es excelente para automatización y DevOps")
    elif lenguaje == "JavaScript":
        print("🟨 JavaScript es ideal para aplicaciones web")
    elif lenguaje == "Go":
        print("🐹 Go es perfecto para sistemas rápidos y concurrentes")
    else:
        print("ℹ️ Lenguaje no reconocido")

if __name__ == "__main__":
    main()
