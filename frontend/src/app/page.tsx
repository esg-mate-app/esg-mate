'use client'

import { useState } from 'react'

export default function Home() {
  const [language, setLanguage] = useState<'EN' | 'ES'>('EN')
  const [activeTab, setActiveTab] = useState<'중대성평가' | 'GRI' | 'TCFD'>('중대성평가')

  return (
    <div className="min-h-screen bg-white">
      {/* Header */}
      <header className="sticky top-0 z-50 bg-white border-b border-gray-100 shadow-sm">
        <div className="max-w-7xl mx-auto flex justify-between items-center px-6 py-6">
          {/* Logo */}
          <div className="text-2xl font-bold text-gray-800 tracking-tight">Marketing</div>
          
          {/* Navigation */}
          <nav className="hidden md:flex gap-8 items-center">
            <a href="#home" className="text-gray-600 hover:text-gray-800 font-medium transition-colors duration-200 text-sm">Home</a>
            <a href="#blog" className="text-gray-600 hover:text-gray-800 font-medium transition-colors duration-200 text-sm">Blog</a>
            <a href="#properties" className="text-gray-600 hover:text-gray-800 font-medium transition-colors duration-200 text-sm">Properties</a>
            <a href="#about" className="text-gray-600 hover:text-gray-800 font-medium transition-colors duration-200 text-sm">About</a>
            <a href="#github" className="text-gray-600 hover:text-gray-800 font-medium transition-colors duration-200 text-sm">GitHub</a>
          </nav>
          
          {/* Language Selector */}
          <div className="flex gap-1">
            <button 
              className={`px-3 py-2 rounded text-sm font-medium transition-all duration-200 ${
                language === 'EN' 
                  ? 'bg-gray-800 text-white shadow-sm' 
                  : 'bg-white text-gray-600 border border-gray-200 hover:border-gray-300 hover:text-gray-800'
              }`}
              onClick={() => setLanguage('EN')}
            >
              EN
            </button>
            <button 
              className={`px-3 py-2 rounded text-sm font-medium transition-all duration-200 ${
                language === 'ES' 
                  ? 'bg-gray-800 text-white shadow-sm' 
                  : 'bg-white text-gray-600 border border-gray-200 hover:border-gray-300 hover:text-gray-800'
              }`}
              onClick={() => setLanguage('ES')}
            >
              ES
            </button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 flex items-center justify-center px-6 py-20">
        <div className="text-center max-w-4xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-bold text-gray-800 mb-8 leading-tight tracking-tight">
            Build Something Amazing
          </h1>
          <p className="text-lg md:text-xl text-gray-600 leading-relaxed max-w-2xl mx-auto font-normal">
            Must today firm from bag. Investment try cold a when capital. Everything wait person service.
          </p>
        </div>
      </main>

      {/* ESG Tabs Section */}
      <section className="px-6 py-16 bg-gray-50">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-800 mb-4">
              ESG Framework
            </h2>
            <p className="text-lg text-gray-600 max-w-2xl mx-auto">
              Choose your ESG assessment framework to get started
            </p>
          </div>
          
          {/* Tabs */}
          <div className="flex justify-center mb-8">
            <div className="bg-white rounded-xl p-2 shadow-lg border border-gray-200">
              {(['중대성평가', 'GRI', 'TCFD'] as const).map((tab) => (
                <button
                  key={tab}
                  onClick={() => setActiveTab(tab)}
                  className={`px-6 py-3 rounded-lg font-medium transition-all duration-200 ${
                    activeTab === tab
                      ? 'bg-blue-600 text-white shadow-md'
                      : 'text-gray-600 hover:text-gray-800 hover:bg-gray-100'
                  }`}
                >
                  {tab}
                </button>
              ))}
            </div>
          </div>
          
          {/* Tab Content */}
          <div className="bg-white rounded-2xl p-8 shadow-lg border border-gray-200">
            {activeTab === '중대성평가' && (
              <div className="text-center">
                <h3 className="text-2xl font-bold text-gray-800 mb-4">중대성평가 (Materiality Assessment)</h3>
                <p className="text-gray-600 mb-6">
                  조직의 핵심 ESG 이슈를 식별하고 우선순위를 설정하는 체계적인 평가 프로세스입니다.
                </p>
                <div className="grid md:grid-cols-3 gap-6">
                  <div className="p-4 bg-blue-50 rounded-lg">
                    <h4 className="font-semibold text-blue-800 mb-2">이해관계자 참여</h4>
                    <p className="text-sm text-blue-700">주요 이해관계자와의 대화를 통한 이슈 식별</p>
                  </div>
                  <div className="p-4 bg-green-50 rounded-lg">
                    <h4 className="font-semibold text-green-800 mb-2">비즈니스 영향</h4>
                    <p className="text-sm text-green-700">재무적, 운영적 관점에서의 영향도 분석</p>
                  </div>
                  <div className="p-4 bg-purple-50 rounded-lg">
                    <h4 className="font-semibold text-purple-800 mb-2">우선순위 설정</h4>
                    <p className="text-sm text-purple-700">중요도와 영향도를 고려한 이슈 우선순위화</p>
                  </div>
                </div>
              </div>
            )}
            
            {activeTab === 'GRI' && (
              <div className="text-center">
                <h3 className="text-2xl font-bold text-gray-800 mb-4">GRI (Global Reporting Initiative)</h3>
                <p className="text-gray-600 mb-6">
                  지속가능성 보고를 위한 글로벌 표준으로, ESG 성과를 체계적으로 측정하고 보고합니다.
                </p>
                <div className="grid md:grid-cols-3 gap-6">
                  <div className="p-4 bg-blue-50 rounded-lg">
                    <h4 className="font-semibold text-blue-800 mb-2">환경 (Environmental)</h4>
                    <p className="text-sm text-blue-700">기후변화, 자원사용, 생물다양성 등</p>
                  </div>
                  <div className="p-4 bg-green-50 rounded-lg">
                    <h4 className="font-semibold text-green-800 mb-2">사회 (Social)</h4>
                    <p className="text-sm text-green-700">노동권, 인권, 지역사회 등</p>
                  </div>
                  <div className="p-4 bg-purple-50 rounded-lg">
                    <h4 className="font-semibold text-purple-800 mb-2">거버넌스 (Governance)</h4>
                    <p className="text-sm text-purple-700">윤리경영, 투명성, 책임성 등</p>
                  </div>
                </div>
              </div>
            )}
            
            {activeTab === 'TCFD' && (
              <div className="text-center">
                <h3 className="text-2xl font-bold text-gray-800 mb-4">TCFD (Task Force on Climate-related Financial Disclosures)</h3>
                <p className="text-gray-600 mb-6">
                  기후변화 관련 재무정보 공개를 위한 국제 표준으로, 기후 리스크와 기회를 체계적으로 관리합니다.
                </p>
                <div className="grid md:grid-cols-4 gap-4">
                  <div className="p-4 bg-blue-50 rounded-lg">
                    <h4 className="font-semibold text-blue-800 mb-2">거버넌스</h4>
                    <p className="text-sm text-blue-700">기후 관련 리스크와 기회에 대한 감독</p>
                  </div>
                  <div className="p-4 bg-green-50 rounded-lg">
                    <h4 className="font-semibold text-green-800 mb-2">전략</h4>
                    <p className="text-sm text-green-700">기후 관련 위험과 기회의 비즈니스 영향</p>
                  </div>
                  <div className="p-4 bg-yellow-50 rounded-lg">
                    <h4 className="font-semibold text-yellow-800 mb-2">리스크 관리</h4>
                    <p className="text-sm text-yellow-700">기후 관련 리스크 식별, 평가, 관리</p>
                  </div>
                  <div className="p-4 bg-red-50 rounded-lg">
                    <h4 className="font-semibold text-red-800 mb-2">지표 및 목표</h4>
                    <p className="text-sm text-red-700">기후 관련 위험과 기회 측정 및 모니터링</p>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </section>

      {/* Bottom Abstract Image */}
      <div className="px-6 pb-12">
        <div className="max-w-6xl mx-auto">
          <div className="w-full h-80 md:h-96 rounded-2xl overflow-hidden bg-gradient-to-br from-gray-50 via-gray-100 to-gray-200 relative shadow-lg">
            {/* Abstract Pattern Layers */}
            <div className="absolute inset-0 bg-gradient-to-br from-white/90 via-white/70 to-white/50"></div>
            <div className="absolute inset-0 bg-gradient-to-br from-white/60 via-transparent to-white/40"></div>
            <div className="absolute inset-0 bg-gradient-to-br from-transparent via-white/30 to-white/50"></div>
            <div className="absolute inset-0 bg-gradient-to-br from-white/40 via-transparent to-white/30"></div>
            
            {/* Grid Pattern */}
            <div className="absolute inset-0 opacity-20">
              <div className="w-full h-full bg-[repeating-linear-gradient(90deg,transparent,transparent_40px,rgba(255,255,255,0.3)_40px,rgba(255,255,255,0.3)_80px),repeating-linear-gradient(0deg,transparent,transparent_40px,rgba(255,255,255,0.3)_40px,rgba(255,255,255,0.3)_80px)]"></div>
            </div>
            
            {/* Floating Elements */}
            <div className="absolute top-1/4 left-1/4 w-32 h-32 bg-white/20 rounded-full blur-sm"></div>
            <div className="absolute top-1/3 right-1/3 w-24 h-24 bg-white/30 rounded-full blur-sm"></div>
            <div className="absolute bottom-1/4 left-1/3 w-20 h-20 bg-white/25 rounded-full blur-sm"></div>
          </div>
        </div>
      </div>
    </div>
  )
}
