import Header from "@/components/Header";
import HeaderNotLogged from "@/components/HeaderNotLogged";
import Footer from "@/components/Footer";

let logado = true

export default function seuprogresso() {
    if (logado) {
        return (
            <div>
                <Header/>
                <Footer/>
            </div>
        )
    }
    return (
        <div>
            <HeaderNotLogged/>
            <Footer/>
        </div>
    )
}