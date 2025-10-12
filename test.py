import subprocess

choices = ["Option 1", "Option 2", "Option 3"]

# Run fzf with the choices
fzf = subprocess.run(
    ["fzf", "--prompt=Choose an option: "],
    input="\n".join(choices).encode(),  # pass choices as input
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Get the selected option
selected = fzf.stdout.decode().strip()

print("You selected:", selected)
