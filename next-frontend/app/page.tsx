import HeaderNotLogged from "@/components/HeaderNotLogged";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

let logado = true

export default function Home() {
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
  );
}
