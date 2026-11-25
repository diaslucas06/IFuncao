"use client";

import { useState, useEffect, Suspense } from "react";
import { useSearchParams, useRouter } from "next/navigation";
import ContentSummary from "@/components/ContentSummary";
import Header from "@/components/Header";
import CardRelatedContent from "@/components/CardRelatedContent";
import dynamic from "next/dynamic";

const PdfSlideViewer = dynamic(() => import("@/components/PdfSlideViewer"), { ssr: false });

const ARQUIVOS_SLIDES: Record<number, string> = {
  1: "grandezas.pdf",
  2: "razao-proporcao.pdf",
  3: "conjuntos.pdf",
  4: "fracoes-intervalos.pdf",
  5: "teorema-tales.pdf",
  6: "trigonometria.pdf",
  7: "funcao-afim.pdf",
  8: "funcao-quadratica.pdf",
};

function ConteudoDetalhe() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const etapa = searchParams.get("etapa") || "1";
  const nome = searchParams.get("nome");

  const [conteudo, setConteudo] = useState<any>(null);
  const [carregando, setCarregando] = useState(true);
  const [finalizando, setFinalizando] = useState(false);
  const [finalizado, setFinalizado] = useState(false);

  useEffect(() => {
    if (!nome) {
      setCarregando(false);
      return;
    }

    const dadosUsuario = localStorage.getItem("usuario");
    const token = dadosUsuario ? JSON.parse(dadosUsuario).access_token : "";
    const headers = { Authorization: `Bearer ${token}` };

    fetch(`http://localhost:8000/conteudos/buscar?q=${encodeURIComponent(nome)}`, { headers })
      .then((res) => res.json())
      .then((resultados) => {
        const alvo = resultados[0];
        if (!alvo) {
          setConteudo(null);
          setCarregando(false);
          return;
        }

        fetch(`http://localhost:8000/conteudos/${alvo.cont_etapa}`, { headers })
          .then((res) => res.json())
          .then((lista) => {
            const encontrado = lista.find((item: any) => item.cont_id === alvo.cont_id);
            setConteudo(encontrado || null);
            setCarregando(false);
          })
          .catch(() => setCarregando(false));
      })
      .catch(() => setCarregando(false));
  }, [etapa, nome]);

  const finalizarConteudo = async () => {
    if (!conteudo || finalizando || finalizado) return;
    setFinalizando(true);

    const dadosUsuario = localStorage.getItem("usuario");
    const token = dadosUsuario ? JSON.parse(dadosUsuario).access_token : "";

    if (!token) {
      alert("Sua sessão expirou. Faça login novamente.");
      router.push("/login");
      setFinalizando(false);
      return;
    }

    const etapaAtual = String(conteudo.cont_etapa || etapa);
    const nomeConteudo = encodeURIComponent(conteudo.cont_nome);

    try {
      const resposta = await fetch(
        `http://localhost:8000/conteudos/finalizar?cont_nome=${nomeConteudo}`,
        {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      if (resposta.ok) {
        setFinalizado(true);
        const nomeArquivo = ARQUIVOS_SLIDES[conteudo.cont_id];
        if (nomeArquivo) {
          sessionStorage.removeItem(`slide_atual_/slides/etapa-${etapaAtual}/${nomeArquivo}`);
        }
        setTimeout(() => router.push(`/conteudos`), 2000);
      } else if (resposta.status === 401) {
        localStorage.removeItem("usuario");
        alert("Sua sessão expirou. Faça login novamente.");
        router.push("/login");
      } else {
        const erroApi = await resposta.json().catch(() => null);
        alert(erroApi?.detail || "Não foi possível finalizar o conteúdo. Tente novamente.");
      }
    } catch {
      alert("Erro de conexão ao tentar finalizar o conteúdo.");
    } finally {
      setFinalizando(false);
    }
  };

  if (carregando) return <div>Carregando...</div>;

  if (!conteudo) {
    return (
      <div>
        <Header />
        <main className="p-10 text-center font-bold text-xl">Conteúdo não encontrado.</main>
      </div>
    );
  }

  const etapaAtual = conteudo.cont_etapa || etapa;

  const dadosResumo = {
    id: conteudo.cont_id,
    titulo: conteudo.cont_nome,
    conteudo: conteudo.cont_texto,
  };

  const listaBruta = Array.isArray(conteudo.cont_relacionados)
    ? conteudo.cont_relacionados
    : conteudo.cont_relacionados?.topicos || conteudo.cont_relacionados?.relacionados || [];

  const dadosRelacionados = {
    id: conteudo.cont_id,
    etapa: etapaAtual,
    relacionados: listaBruta.map((item: any, i: number) => ({
      id: item.cont_id ?? item.id ?? i,
      titulo: typeof item === "string" ? item : item.cont_nome ?? item.titulo,
      etapa: item.cont_etapa ?? etapaAtual,
    })),
  };

  const nomeArquivo = ARQUIVOS_SLIDES[conteudo.cont_id];
  const urlPdf = nomeArquivo ? `/slides/etapa-${etapaAtual}/${nomeArquivo}` : "";

  return (
    <div>
      <Header />
      <main className="p-5 mt-2 sm:mt-6 mx-5">
        <ContentSummary dados={dadosResumo} />

        <div className="w-full flex flex-col lg:flex-row gap-6 lg:items-start">
          <div className="w-full lg:w-2/3 lg:mt-4 min-w-0">
            {urlPdf && (
              <PdfSlideViewer
                pdfUrl={urlPdf} onFinalizar={finalizarConteudo} finalizando={finalizando} finalizado={finalizado}
              />
            )}
          </div>

          <div className="w-full lg:w-1/3 lg:mt-4 min-w-0">
            <CardRelatedContent conteudo={dadosRelacionados} />
          </div>
        </div>
      </main>
    </div>
  );
}

export default function Conteudos() {
  return (
    <Suspense fallback={<div>Carregando...</div>}>
      <ConteudoDetalhe />
    </Suspense>
  );
}