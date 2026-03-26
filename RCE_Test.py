import azure.functions as func
import os
import logging

# GitHub Açıklaması: Bu PoC, kullanıcı girişlerinin (JSON) doğrudan sistem komutlarına 
# aktarılmasının (Unsafe Deserialization) yarattığı RCE riskini göstermek içindir.

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="ExploitTrigger")
def ExploitTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('PoC Test: Insecure Command Execution Analysis.')
    
    try:
        # 1. Adım: Kullanıcıdan JSON verisini al
        req_body = req.get_json()
        command_key = req_body.get('command')
        
        # 2. Adım: Zafiyet Noktası - Gelen veri sanitize edilmeden os.system'e gidiyor
        if command_key == "calc":
            # Yerel test ortamında hesap makinesini tetikler
            # Gerçek senaryolarda bu bir RCE zafiyetidir.
            os.system("gnome-calculator &") 
            
            return func.HttpResponse(
                "PoC Successful: System command executed via RCE vulnerability.",
                status_code=200
            )
        
        return func.HttpResponse("Valid command not found.", status_code=400)

    except Exception as e:
        return func.HttpResponse(f"Error during execution: {str(e)}", status_code=500)