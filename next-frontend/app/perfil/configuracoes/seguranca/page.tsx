import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Sidebar from "@/components/Sidebar";

export default function seguranca() {
    return (
        <div>
            <Header/>
            <div className="flex">
                <Sidebar/>
            </div>
            <Footer/>
        </div>
    )
}