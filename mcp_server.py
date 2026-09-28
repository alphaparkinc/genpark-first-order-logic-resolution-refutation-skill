"""MCP stdio server for First-Order Logic Unifier."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import FOLUnifier

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "unify_terms",
                        "description": "Compute Robinson Most General Unifier (MGU) between two first-order terms",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "term1": {"description": "Term 1 (variables start with ?)"},
                                "term2": {"description": "Term 2"}
                            },
                            "required": ["term1", "term2"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "unify_terms":
            t1 = args.get("term1")
            t2 = args.get("term2")
            mgu = FOLUnifier.unify(t1, t2)
            if mgu is None:
                return {"jsonrpc": "2.0", "id": req_id, "result": {"unifiable": False, "substitutions": None}}
            return {"jsonrpc": "2.0", "id": req_id, "result": {"unifiable": True, "substitutions": mgu}}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
