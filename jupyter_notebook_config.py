# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'openrefine': {
        'command': ['/home/jovyan/.openrefine/openrefine-3.5.0/refine', '-p', '{port}','-d','/home/jovyan/openrefine', '-i', '0.0.0.0'],
        'port': 3333,
        'timeout': 120,
        'launcher_entry': {
            'title': 'OpenRefine'
        },
    },
}
