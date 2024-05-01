def jointure(emails_ids, ids_pseudos):
    result = {}
    for k, v in emails_ids.items():
        if v in ids_pseudos.keys():
            result[k] = ids_pseudos[v]
        else:
            result[k] = k
    return result

# Tests

emails_ids = {"alice@fake.com": 1, "bob@bidon.fr": 2, "chris@false.uk": 3}
ids_pseudos = {1: "alice", 2: "B0b", 3: "ChristoF"}
assert jointure(emails_ids, ids_pseudos) == {
    "alice@fake.com": "alice",
    "bob@bidon.fr": "B0b",
    "chris@false.uk": "ChristoF",
}

emails_ids = {"alice@fake.com": 1, "bob@bidon.fr": 2, "chris@false.uk": 3}
ids_pseudos = {1: "alice", 2: "B0b"}
assert jointure(emails_ids, ids_pseudos) == {
    "alice@fake.com": "alice",
    "bob@bidon.fr": "B0b",
    "chris@false.uk": "chris@false.uk",
}

emails_ids = {"alice@fake.com": 5, "bob@bidon.fr": 6, "chris@false.uk": 3}
ids_pseudos = {5: "Alic3", 3: "ChristoF"}
assert jointure(emails_ids, ids_pseudos) == {
    "alice@fake.com": "Alic3",
    "bob@bidon.fr": "bob@bidon.fr",
    "chris@false.uk": "ChristoF",
}
