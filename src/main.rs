use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};

#[get("/")]
async fn hello() -> impl Responder {
    HttpResponse::Ok().body("Hello World")
}

#[post("/echo")]
async fn echo(req_body: String) -> impl Responder {
    HttpResponse::Ok().body(req_body)
}

async fn manual_hello() -> impl Responder {
    HttpResponse::Ok().body("Hello World")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(hello)
            .service(echo)
            .route("hey", web::get().to(manual_hello))

    })
    .bind(("127.0.0.1", 8021))?
    .run()
    .await
}

/* Unit Tests */

#[cfg(test)]
mod tests {
    #[test]
    fn hello_test() {
        let hello_world: &str = "Hello World";
        assert_eq!(hello_world, "Hello World");
    }
}