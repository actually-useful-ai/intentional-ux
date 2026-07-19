# Intentional UX

Intentional UX analyzes the latency between a person's intention and a confirmed
outcome. It turns a product journey into a task path, identifies avoidable
interaction cost, and makes recommendations that remain traceable to evidence.

## What it evaluates

Each review considers a vector of related concerns instead of hiding trade-offs
inside one score:

- completion and success evidence;
- hit count and corrective interactions;
- Fitts's law when target distance and effective width are measured;
- cognitive load, waits, context switches, and recovery cost;
- surface economy without sacrificing discovery or control;
- accessibility across relevant people and input modes; and
- frontend integrity across CSS, DOM, events, focus, and state.

## Add to Codex

In the Codex app, open the Plugin Directory, choose its import option, and use
this repository's URL or a local checkout. Codex discovers the package through
`.codex-plugin/plugin.json`.

For a direct personal installation on a Codex setup that does not offer plugin
import, clone the repository, enter its directory, and create a guarded link:

```sh
mkdir -p "$HOME/.agents/skills"
if [ -e "$HOME/.agents/skills/intentional-ux" ] || [ -L "$HOME/.agents/skills/intentional-ux" ]; then
  echo "intentional-ux is already installed; leaving it unchanged"
else
  ln -s "$PWD/skills/intentional-ux" "$HOME/.agents/skills/intentional-ux"
fi
```

The guard preserves an existing file, directory, or symbolic link.

## Add to Claude Code

Add this repository as a marketplace, then install the package:

```text
/plugin marketplace add actually-useful-ai/intentional-ux
/plugin install intentional-ux@intentional-ux
```

## Attribution

Created by Luke Steuber.
